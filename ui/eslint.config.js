import pluginJs from '@eslint/js'
import pluginVue from 'eslint-plugin-vue'
import ts from 'typescript-eslint'
import vueEslintConfigTypescript from '@vue/eslint-config-typescript'
import configPrettier from 'eslint-config-prettier'

export default [
  pluginJs.configs.recommended,
  ...ts.configs.recommended,
  ...vueEslintConfigTypescript(),
  ...pluginVue.configs['flat/recommended'],
  configPrettier,
  {
    files: ['*.vue', '**/*.vue'],
    rules: {
      'vue/multi-word-component-names': 'off',
    },
  },
  {
    ignores: ['dist/', 'node_modules/', '*.lock', '.gitignore'],
  },
  {
    rules: {
      '@typescript-eslint/no-unused-vars': [
        'error',
        { argsIgnorePattern: '^_' },
      ],
      '@typescript-eslint/no-explicit-any': 'warn',
      'vue/require-default-props': 'off',
      'vue/require-explicit-emits': 'off',
    },
  },
]
