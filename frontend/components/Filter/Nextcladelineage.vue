<template>
	<b-field expanded>
		<template #label>
			Nextclade assigned lineage
			<b-tooltip type="is-dark" label="Help text here for explanation">
				<b-icon size="is-small" icon="help-circle-outline"></b-icon>
			</b-tooltip>
		</template>
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			icon="filter"
			v-model="tags"
			type="is-cyan"
			:data="filtered"
			@typing="Filtering"
			close-type="is-dark"
			:placeholder="tags.length ? '' : 'Type a lineage name'"
		/>
	</b-field>
</template>

<script>
export default {
	data: () => ({
		tags: [],
		state: [],
		filtered: [],
	}),
	props: {
		value: { type: Array, required: true },
		options: { type: Array, required: true },
	},
	watch: {
		tags(value) {
			this.$emit('input', value)
		},
		options(value) {
			this.state = value
		},
		value(value) {
			this.tags = value
		},
	},
	methods: {
		Filtering(text) {
			this.filtered = this.state.filter((d) => d.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0)
		},
	},
	mounted() {
		this.$nextTick(async () => {
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
